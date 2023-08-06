import csv
import json
import os
import random
import threading
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import requests
import validators
import yaml
from tqdm import tqdm

from pyronos.user_agents import USER_AGENTS

plt.switch_backend('Agg')
VERSION = '0.0.1'
AVAILABLE_METHODS = ['get', 'head', 'options', 'delete', 'post', 'put']
AVAILABLE_FIGURES = ['simple', 'stem', 'step']
AVAILABLE_OUTPUTS = ['csv', 'json', 'yml']


class Pyronos():
    def __init__(self, url='', method='',
                 data={}, headers={},
                 timeout=30, num_requests=1,
                 figure='', output='',
                 sequential=False, print_progress=False,
                 dump_log=False):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.url = url
        if not validators.url(self.url):
            raise ValueError(self.url, 'URL not valid!')
        self.figure = figure
        if self.figure != '' and self.figure.lower() not in AVAILABLE_FIGURES:
            raise ValueError(self.figure, 'Figure type not found in available figure types!', AVAILABLE_FIGURES)
        self.output = output
        if self.output != '' and self.output.lower() not in AVAILABLE_OUTPUTS:
            raise ValueError(self.output, 'Output type not found in available output types!', AVAILABLE_OUTPUTS)
        self.method = method
        if self.method != '' and self.method.lower() not in AVAILABLE_METHODS:
            raise ValueError(self.method, 'Method not found in available methods!', AVAILABLE_METHODS)
        self.headers = headers
        # Lower case all headers.
        self.headers = {k.lower(): v for k, v in self.headers.items()}
        # If user-agent not found in headers, select random one from user_agents file.
        if 'user-agent' not in self.headers:
            self.headers['user-agent'] = random.choice(USER_AGENTS)
        self.starting_timestamp = str(time.time()).split('.')[0]
        self.starting_time = dt_string
        self.domain = self.url.split('://')[1].replace('.', '_')
        self.timeout = timeout
        self.data = data
        self.num_requests = num_requests
        self.sequential = sequential
        self.figure = figure
        self.output = output
        self.print_progress = print_progress
        self.log = dump_log
        self.error_messages = []
        self.response_times = []
        self.response_codes = []
        self.num_failed_responses = 0
        self.quartiles = []
        self.first_quartile = 0
        self.median = 0
        self.third_quartile = 0
        self.std = 0
        self.results = None
        self.STATE = 'BUSY'

    def dispatcher(self):
        if self.sequential and self.print_progress:
            for _ in tqdm(range(self.num_requests)):
                req_thread = threading.Thread(target=self.start)
                req_thread.start()
                req_thread.join()
        else:
            print('WARNING: To print progress you have to send sequential requests!')
            for _ in range(self.num_requests):
                req_thread = threading.Thread(target=self.start)
                req_thread.start()
                req_thread.join()

    def start(self):
        try:
            if self.method == 'get':
                response = requests.get(self.url, self.headers, timeout=self.timeout)
            elif self.method == 'head':
                response = requests.head(self.url, headers=self.headers, timeout=self.timeout)
            elif self.method == 'options':
                response = requests.options(self.url, headers=self.headers, timeout=self.timeout)
            elif self.method == 'delete':
                response = requests.delete(self.url, headers=self.headers, timeout=self.timeout)
            elif self.method == 'post':
                response = requests.post(self.url, headers=self.headers, data=self.data, timeout=self.timeout)
            elif self.method == 'put':
                response = requests.put(self.url, headers=self.headers, data=self.data, timeout=self.timeout)
            self.response_times.append(response.elapsed.total_seconds())
            self.response_codes.append(response.status_code)
        except Exception as RequestError:
            self.error_messages.append(str(RequestError))
            self.num_failed_responses += 1
        finally:
            self.end()

    def end(self):
        if len(self.response_times) == self.num_requests or self.num_failed_responses == self.num_requests:
            handle_res_thread = threading.Thread(target=self.handle_results)
            handle_res_thread.start()
            handle_res_thread.join()
            self.STATE = 'READY'

    def save_results(self):
        filename = 'results/outputs/'+self.domain+'_'+self.starting_timestamp+'.'+self.output
        if self.output == 'csv':
            with open(filename, mode='w') as results_csv_file:
                results_writer = csv.writer(results_csv_file, delimiter=',')
                results_writer.writerow(['request_id', 'response_time', 'response_code'])
                for res_id, res_time in enumerate(self.response_times):
                    results_writer.writerow([res_id, res_time, self.response_codes[res_id]])
        elif self.output == 'json':
            with open(filename, 'w') as results_json_file:
                results_json = json.dumps(self.results)
                json.dump(results_json, results_json_file)
        elif self.output == 'yml':
            with open(filename, 'w') as results_yml_file:
                yaml.dump(self.results, results_yml_file, default_flow_style=False)

    def draw_results(self):
        filename = 'results/figures/'+self.domain+'_'+self.starting_timestamp+'_'+self.figure+'.png'
        x = range(self.num_requests)
        y = self.response_times
        fig, ax = plt.subplots()
        plt.xticks(np.arange(min(x), max(x) + 1, 5.0), fontsize=8, rotation='45')
        plt.margins(0.01)
        ax.plot(x, y)
        ax.grid()
        ax.set(xlabel='Request ID', ylabel='Response Time (s)', title='Pyronos v{}'.format(VERSION))
        if self.figure == 'simple':
            # Pass for simple plotting.
            pass
        elif self.figure == 'step':
            plt.step(x, y)
        elif self.figure == 'stem':
            plt.stem(x, y)
        fig.savefig(filename)

    def dump_logs(self):
        filename = 'results/logs/'+self.domain+'_'+self.starting_timestamp+'.log'
        with open(filename, 'w') as log_file:
            log_file.write(str(self.results)+'\n')
            log_file.write('\n'.join(self.error_messages))

    def handle_results(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if self.figure != '' or self.output != '' or self.log:
            if not os.path.exists('results'):
                os.makedirs('results')
        if len(self.response_times) != 0:
            self.quartiles = np.percentile(self.response_times, [25, 50, 75], interpolation='midpoint')
            self.quartiles = list(map(lambda x: float(x), self.quartiles))
            self.first_quartile = self.quartiles[0]
            self.median = self.quartiles[1]
            self.third_quartile = self.quartiles[2]
            self.std = float(np.std(self.response_times))
            if self.figure != '':
                if not os.path.exists('results/figures'):
                    os.makedirs('results/figures')
                fig_thread = threading.Thread(target=self.draw_results)
                fig_thread.start()
            if self.output != '':
                if not os.path.exists('results/outputs'):
                    os.makedirs('results/outputs')
                out_thread = threading.Thread(target=self.save_results)
                out_thread.start()
        self.results = {
            'starting_time': self.starting_time,
            'finishing_time': dt_string,
            'response_times': self.response_times,
            'response_codes': self.response_codes,
            'num_of_failed_responses': self.num_failed_responses,
            'q1': self.first_quartile,
            'median': self.median,
            'q3': self.third_quartile,
            'std': self.std
        }
        if self.log:
            if not os.path.exists('results/logs'):
                os.makedirs('results/logs')
            log_thread = threading.Thread(target=self.dump_logs)
            log_thread.start()
