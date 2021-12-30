# 🧨  RChecker v1.0

<h3> Checker for Minecraft Servers </h3>
<br/>
</br>
<p align="center">
<img src="https://github.com/wrrulos/Imagenes-Github/blob/main/RChecker/RChecker.PNG" title="RChecker">
</p>
<br/>

## 💻 Supported operating systems:

* ✅ Windows (8, 8.1, 10 and 11)
* ✅ Linux
* ✅ Termux

# 🔧 Installation 

```bash
# Clone the repository
$ git clone https://github.com/wrrulos/RSubd

# Go into the RSubd folder
$ cd RSubd

# Install the requirements
$ python3 -m pip install -r requirements.txt

```
# 🕹 Usage

```bash
$ python3 RChecker.py -h
usage: RChecker.py [-h] -f FILE [--timeout TIMEOUT] [--no-output]

options:
  -h, --help         show this help message and exit
  -f FILE            File name
  --timeout TIMEOUT  Server ping timeout (default is 2)
  --no-output        Prevents RChecker from saving the results to a text file
  
```
Check the file "Scan.txt"
```
python3 RChecker.py -f Scan.txt
```
Check the file "Scan.txt" and set a timeout of 3 seconds
```
python3 RChecker.py -f Scan.txt --timeout 3
```
Check the "Scan.txt" file and prevent RChecker from saving the results to a text file
```
python3 RChecker.py -f Scan.txt --no-output
```

## 📸 Gif

<img src="https://github.com/wrrulos/Imagenes-Github/blob/main/RChecker/RChecker.gif">

## Licencia 

MIT License

Copyright (c) 2021 Pedro Vega

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

 
