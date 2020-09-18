from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import random
import time
import json
from django.core.cache import cache, caches
from django.urls import reverse
from django.shortcuts import render, redirect


class HelloMiddle(MiddlewareMixin):

    def process_request(self, request):
        cache_mode = caches['redis_drive']
        print(request.META.get('REMOTE_ADDR'))
        ip = request.META.get('REMOTE_ADDR')
        if ip == '127.0.0.1' and request.path == '/app/get_prize/':
            if random.randrange(100) > 50:
                return HttpResponse('50 middle bingo')
            if random.randrange(100) > 30:
                return HttpResponse('30 middle bingo')

        elif str(ip).startswith('127.0.0') and request.path == '/app/get_ticket/':
            return HttpResponse('已搶完')

        elif request.path == '/app/search/':
            search_ip = ip + 'search'
            result = cache_mode.get(search_ip)
            if result:
                return HttpResponse('搜尋過於頻繁，10秒後再次搜尋')
            cache_mode.set(search_ip, ip, timeout=10)

        elif request.path == '/app/sequence_time/':
            sequence_time_ip = ip + 'sequence_time_ip'
            black_list = cache_mode.get('black_list', {})
            print(black_list)

            if ip in black_list:
                if time.time() > black_list[ip]:
                    del black_list[ip]
                    cache_mode.set('black_list', black_list)
                else:
                    return HttpResponse('黑名單')

            result = cache_mode.get(sequence_time_ip, [])

            while result and time.time() - result[-1] > 60:
                result.pop()

            result.insert(0, time.time())
            cache_mode.set(sequence_time_ip, result, timeout=60)

            if len(result) > 30:
                black_list.update({ip: time.time() + 60 * 60 * 24})
                cache_mode.set('black_list', black_list, timeout=60 * 60 * 24)
                return HttpResponse('黑名單')
            elif len(result) > 10:
                return HttpResponse('1分鐘內過於頻繁')

    def process_exception(self, request, exception):
        print('process_exception', request, exception)
        return redirect(reverse('app:ip'))


class AgainMiddle(MiddlewareMixin):

    def process_request(self, request):
        print('AgainMiddle')
