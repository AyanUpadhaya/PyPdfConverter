# Webpage to pdf converter
# local web page to pdf converter
# python application using pdfcrowd module: 'pip install pdfcrowd' 
# API-application programming interface

"""IMPORTANT THING - SAVE AS .pdf file"""

import pdfcrowd
import sys
import os

API_NAME= 'demo'
API_KEY= "ce544b6ea52a5621fb9d55f8b542d14d"

#convert web to pdf
def convertWebToPdf(url,filename):
	#filename = converted file name, extension as .pdf 
	try:
		api_client = pdfcrowd.HtmlToPdfClient(API_NAME, API_KEY)
		api_client.convertUrlToFile(url, filename)

	except pdfcrowd.Error as why:
		#report the Error

		sys.stderr.write("PdfCrowd Error: {}\n".format(why))

#covert local html file to pdf
def convertHTMLtoPdf(localHTML,filename):
	#localHTML = local html web page path
	#filename = converted file name, extension as .pdf
	try:
		api_client = pdfcrowd.HtmlToPdfClient(API_NAME, API_KEY)
		api_client.convertFileToFile(localHTML, filename)

	except pdfcrowd.Error as why:
		#report the Error
		sys.stderr.write("PdfCrowd Error: {}\n".format(why))

run = True
while run:
	print("Welcom to PdfCrowd Converter")
	print("=============================")
	print("Press i to convert web to pdf")
	print("Press h to convert local html page to pdf")
	print("Press q to quit")
	option=input('>')

	if option == "i":
		url_address=input("Enter url:")
		file_name=input("Save as:")
		if 'pdf' in file_name: 
			convertWebToPdf(url_address,file_name)
			print("Success !")
			print()
		else:
			print("wrong extension")
			continue
	elif option == "h":
		localfile=input("Path of Html:")
		file_name=input("Save as:")
		if 'pdf' in file_name: 
			convertHTMLtoPdf(localfile,file_name)
			print("Success !")
			print()
		else:
			print("wrong extension")
			continue

	elif option=='q':
		run=False

	else:
		print("wrong input")
		print()

