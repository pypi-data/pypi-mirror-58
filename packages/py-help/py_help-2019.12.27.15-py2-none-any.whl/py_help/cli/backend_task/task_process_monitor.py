# -*- coding: utf-8 -*-
import threading
import time
import multiprocessing
from multiprocessing import Manager
from .. import debug, info, warn, error
from .task_process import TaskProcess


class TaskProcessMonitor(threading.Thread):
    process_status = {}

    def __init__(self, start_port, process_cnt, the_router_class, is_gevent=False):
        super(TaskProcessMonitor, self).__init__()
        self.start_port = start_port
        self.process_cnt = process_cnt
        self.is_start = True
        self.is_gevent = is_gevent
        self.manager = Manager()
        self.shared_dict = self.manager.dict()
        self.shared_queue_list = []
        self.my_processes = []
        self.running_router_class_name = "{}.{}".format(the_router_class.__module__, the_router_class.__name__)
        thr_pool = multiprocessing.pool.ThreadPool()

        worker_id = 0
        for port in range(start_port, start_port + process_cnt):
            self.shared_queue_list.append(self.manager.Queue(2048))
            proc = TaskProcess(port=port, is_gevent=self.is_gevent, worker_id=worker_id,
                               shared_dict=self.shared_dict,
                               shared_queue_list=self.shared_queue_list,
                               router_class_name=self.running_router_class_name)
            self.my_processes.append(proc)
            worker_id += 1

        for one_process in self.my_processes:
            thr_pool.apply_async(one_process.trigger_start)
        thr_pool.close()
        thr_pool.join()

    def run(self):
        debug("start Monitor {} router:{}".format(self.my_processes, self.running_router_class_name))
        time.sleep(15)  # 这里先等一下,保证进程起来
        while self.is_start:
            try:
                for one_process in self.my_processes:
                    if not one_process.check_is_alive():
                        info("进程不存活:{},启动router:{}".format(one_process, self.running_router_class_name))
                        one_process.trigger_start()
                time.sleep(1)
            except Exception as e:
                error("监控任务出错::", e)
                time.sleep(5)

    def stop(self):
        debug("开始停止")
        self.is_start = False
        for one_process in self.my_processes:
            if one_process.check_is_alive():
                try:
                    one_process.trigger_stop_proc()
                except Exception as ex:
                    error("退出时出错了", ex)
