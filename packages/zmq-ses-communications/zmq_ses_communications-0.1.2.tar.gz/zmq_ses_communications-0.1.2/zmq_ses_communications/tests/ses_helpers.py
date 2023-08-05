#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Message:
    def __init__(self,topic,contents):
        self.topic = topic
        self.contents = contents
    def __str__(self):
    	return str(self.topic)+" : "+str(self.contents)