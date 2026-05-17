#!/usr/bin/python.pydPiper3
# coding: UTF-8

from __future__ import unicode_literals

# Final Page Definitions for 20x4 LCD (100% Webradio Optimized)

FONTS = {
        'small': { 'default':True, 'file':'latin1_5x8_lcd.fnt','size':(5,8) },
        'large': { 'file':'BigFont_10x16_fixed.fnt', 'size':(10,16) },
        'tiny': { 'file':'upperasciiwide_3x5_fixed.fnt', 'size':(5,5) },
}

IMAGES = {
        'progbar': {'file':'progressbar_100x8.png' },
}

WIDGETS = {
        # Beim Booten im Hintergrund, falls das System kurz braucht
        'splash': { 'type':'text', 'format':'pydPiper\nStarting...', 'font':'small' },
        
        # BOOTEN
        'raspdac':  { 'type':'text', 'format':"RASPDAC", 'font':'large', 'varwidth':True, 'size':(100,16), 'just':'center' },
        'ip': { 'type':'text', 'format':'IP: {0}', 'variables':['ip'], 'font':'small', 'varwidth':True, 'just':'center', 'size':(100,8) },
        
        # PLAY-MODUS (Webradio)
        'radio_station': { 'type':'text', 'format':'{0}', 'variables':['artist'], 'font':'small', 'varwidth':True, 'just':'center', 'size':(100,8) },
        'radio_song':    { 'type':'text', 'format':'{0}', 'variables':['title'], 'font':'small', 'varwidth':True, 'just':'center', 'size':(100,8) },
        'radio_bitrate': { 'type':'text', 'format':'{0}', 'variables':['bitrate'], 'font':'small', 'varwidth':True, 'just':'center', 'size':(100,8) },
        
        # STANDBY
        'time': { 'type':'text', 'format':'{0}', 'variables':['localtime|strftime+%-H:%M'], 'font':'large', 'just':'right', 'varwidth':True, 'size':(65,16) }
}

CANVASES = {
        # Start-Sequenz
        'start':      { 'widgets': [ ('raspdac',0,0), ('ip',0,24) ], 'size':(100,32) },
        'blank':      { 'widgets': [], 'size':(100,32) },
        
        # Das Webradio-Wiedergabe-Layout
        'play_radio': { 'widgets': [ 
                ('radio_station',0,0),   # Zeile 1 (Y=0): Sendername
                ('radio_song',0,8),      # Zeile 2 (Y=8): Songtext (Fest, ungescrollt)
                # Zeile 3 (Y=16): Bleibt frei als edle Lücke
                ('radio_bitrate',0,24)   # Zeile 4 (Y=24): Technische Bitrate (z.B. 128 kbs)
        ], 'size':(100,32) },
        
        # Standby
        'stoptime':   { 'widgets': [ ('time',20,8) ], 'size':(100,32) }
}

SEQUENCES = [
        {       'name': 'seqSplash', 'canvases': [ { 'name':'start', 'duration':5 } ], 'conditional': "db['state']=='starting'" },
        {
                'name': 'seqPlay',
                'canvases': [
                        { 'name':'play_radio', 'duration':9999 },
                ],
                'conditional': "db['state']=='play'"
        },
        {
                'name': 'seqStop',
                'canvases': [
                        { 'name':'stoptime', 'duration':9999 }
                ],
                'conditional': "db['state']=='stop' or db['state']=='pause'"
        }
]
