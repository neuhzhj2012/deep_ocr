#coding=utf-8
import os
import ctypes

libname = "/usr/lib/libtesseract.so.3" # tesseract引擎的动态库
lang = "eng" # 识别的语言，eng是英文，chi_sim是中文，自己选择
filename = "test_data.png"  # 待识别图片

# 加载动态库
tesseract = ctypes.cdll.LoadLibrary(libname)
TESSDATA_PREFIX = os.environ.get("TESSDATA_PREFIX")

# 创建一个handle,请看TessBaseAPI,你就懂了为啥非要有handle
api = tesseract.TessBaseAPICreate()

# 初始化引擎
rc = tesseract.TessBaseAPIInit3(api,TESSDATA_PREFIX,lang)

# 处理待识别图片
text_out = tesseract.TessBaseAPIProcessPages(api,filename,None,0)

#转成字符串
result_text = ctypes.string_at(text_out)
print result_text  # 输出结果
