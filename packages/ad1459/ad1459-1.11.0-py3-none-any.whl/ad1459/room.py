#!/usr/bin/env python3

""" AD1459, an IRC Client

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

  Handling for rooms and their messages.
"""

import asyncio
import logging
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .widgets.message_row import MessageRow
from .widgets.room_row import RoomRow, RoomKind

class RoomWindow(Gtk.ScrolledWindow):

    def __init__(self, room):
        super().__init__()
        self.room = room

class Room():
    """ The class to represent a room.

    Attributes: 
        messages (:obj:`Gtk.ListBox`): The list of messages in this room's 
            buffer
        row (:obj:`RoomRow`): The row object for this room in the room list.
    """

    def __init__(self, network):
        self.log = logging.getLogger('ad1459.room')
        self.network = network
        
        self.window = RoomWindow(self)
        self.window.set_vexpand(True)
        self.window.set_hexpand(True)
        self.window.network = self.network
        self.window.room = self

        self.view = Gtk.Viewport()
        self.window.add(self.view)
        self.adj = self.window.get_vadjustment()
        
        self.messages = Gtk.ListBox()
        self.messages.connect('size-allocate', self.on_new_message_scroll)
        self.view.add(self.messages)

        self.adj.connect('value-changed', self.on_window_scrolled)

        self.row = RoomRow(self, self.network, kind='channel')
        self.tab_complete = []
        self.prematched = False
        #self.add_message(f'You have joined')

        # self.populate_test_data()

    @property
    def name(self):
        """str: The name of this room (as displayed in the room list)."""
        return self.row.room_name
    
    @name.setter
    def name(self, name):
        self.row.room_name = name
    
    def part_channel(self, message='Leaving...'):
        """ Exits the channel.
        
        Arguments:
            message (str): A part message for the channel.
        """
        self.log.info('Leaving channel %s (%s)', self.name, message)
        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(
            self.network.client.part(
                self.name,
                message=message
            ),
            loop=loop
        )

    
    def update_tab_complete(self):
        if self.row.kind == RoomKind.CHANNEL:
            self.tab_complete = list(
                self.network.client.channels[self.name]['users']
            )
    
    def print_info(self):
        self.log.info(f'{self.name}, {self.network}')
    
    def on_new_message_scroll(self, window, data=None):
        """ size-allocate signal handler for self.messages."""
        max_value = self.adj.get_upper() - self.adj.get_page_size()
        self.adj.set_value(max_value)

    
    def on_window_scrolled(self, adjstment, data=None):
        """ value-changed signal handler for self.window. """
        max_value = self.adj.get_upper() - self.adj.get_page_size()
        if self.adj.get_value() < max_value:
            try:
                self.messages.disconnect_by_func(self.on_new_message_scroll)
            except TypeError:
                pass
        else:
            try:
                self.messages.disconnect_by_func(self.on_new_message_scroll)
            except TypeError:
                pass
            self.messages.connect('size-allocate', self.on_new_message_scroll)

    def get_messages(self):
        """Get the messages for this room.
        
        Returns:
            :obj:`Gtk.ListBox`: A listbox containing all of the messages.
        """
        return self.messages
    
    def add_message(self, message, sender=None, msg_time=None, css=None):
        """ Adds a new message into this room's buffer.

        Arguments:
            message (str): The message text to add to this room.
            sender (str): The nickname who sent the message, or None for network
                messages.
            msg_time (str): The timestamp of this message, or None for the 
                current time.
            css (str): A CSS class to add to this message.
        """
        if not self.prematched:
            self.update_tab_complete()
            self.prematched = True
        new_message = MessageRow()
        if sender == self.network.nickname:
            css = 'mine'

        if css:
            Gtk.StyleContext.add_class(
                new_message.get_style_context(),
                css
            )

        if msg_time:
            new_message.time = msg_time
        else:
            new_message.time = time.ctime().split()[3]
        
        new_message.sender = '*'
        if sender:
            new_message.sender = sender
        
        new_message.text = message
        
        new_message.show_all_contents()
        self.messages.add(new_message)
        if not sender == '*':
            try:
                self.tab_complete.remove(sender)
                self.tab_complete.insert(0, sender)
                
            except ValueError:
                pass

    def populate_test_data(self):
        
        self.add_message('jeans has joined')
        self.add_message('Hi', sender='jeans')
        self.add_message('hoi', sender='gav')
        self.add_message('How are things', sender='notgav')
        self.add_message('Okay', sender='gav')
        self.add_message(
            (
                'Now it\'s even longer and it will run off the edge of the '
                'boundary so that I can see what it will look like really long. '
                'This is a really long message that I want to send because I '
                'want to see what it looks like in-context. Now it\'s going to '
                'be really long, yay!'
            ), 
            sender='jeans'
        )
        self.add_message('wow spam', sender='gav')
        self.add_message('rood', sender='notgav')
        self.add_message('sorry', sender='jeans')
        self.add_message('bye', sender='gav')
        self.add_message('\\o', sender='notgav')
