# -*- coding: utf-8 -*-
######################################
#                                    #
#### RDS RT Plus Command Generator ###
#         © Mitja Kocjančič          #
######################################

import sys
import time
from collections import Counter
import string
import socket
import errno
import os
import logging

#Some Variables
S_HOST = ''
S_PORT = 4000
C_HOST = 'localhost'
C_PORT = 4001
#Some Variables

#TCP CLIENT PART
def tcp_client(host, port, c_data):
	sock = socket.socket()
	sock.connect((host, port), )
	sock.sendall(c_data)


#TCP CLIENT PART



#TCP SERVER PART (Deprecated)

#HOST = ''
#PORT = 4000

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind((HOST, PORT))  
#sock.listen(100)  
 
#connection,address = sock.accept()  
#TCP SERVER PART (Deprecated)



#DATA RECIEVE
#while True:
#	s = connection.recv(1024)
	#print s
#	RDS(s)
#DATA RECIEVE
#connection.close()

#TCP SERVER PART (Deprecated)



#UDP Server



def udp_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        yield data


#UDP Server






# count
def count_letters(word):
    return len(word) - word.count(' ')

#steje s presledki vred
def stej(word):
    return len(word)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

#RTP Command Generator Function
def RDS (RT_Data):
	#s = "Now playing \+ArMadonna\- - \+TiLike a Virgin\-"
	s = RT_Data
	Artist = find_between( s, "\+Ar", "\-" )
	Title = find_between( s, "\+Ti", "\-" )

	Text = find_between( s, "", "\+Ar" )
	TextCount = stej(Text)

	ArtistL = stej(Artist)-1
	TitleL = stej(Title)-1
	ArtistP = TextCount
	TitleP = ArtistP + ArtistL+1 + 3

	ArtistLen = str(ArtistL)
	TitleLen = str(TitleL)
	ArtistPos = str(ArtistP)
	TitlePos = str(TitleP)



	#Generate RT Command
	RT = "RT=" + Text + Artist + " - " + Title

	#Final RTP Command
	RTPlus = "RTP=" + "4" + "," + ArtistPos + "," + ArtistLen + "," + "1" + "," + TitlePos + "," + TitleLen
	print RT
	print RTPlus
	#Send RadioText
	tcp_client(C_HOST, C_PORT, RT)
	#Send RadioText+
	tcp_client(C_HOST, C_PORT, RTPlus)

#Now playing Madonna - Like a Virgin

#UDP Data
for data in udp_server(S_HOST, S_PORT):
	RDS(data)
	#print data
	#Beležka Ne rabim!! (Logging don't need)	
	#log.debug("%r" % (data,))
	#Beležka Ne rabim!! (Logging don't need)
#UDP Data
