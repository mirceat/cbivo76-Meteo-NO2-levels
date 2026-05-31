# README.md

1. `pip install pandas matplotlib`
2. Remove NUL entries from input txt files - see `prompt-log.md` prompt 16. 

---

```
cd src
python Meteo.py
```

Input folder: `18_0904_0908`  
Output images in: `18_0904_0908out`

---

```
cd src
python MeteoGas.py
```

Input folder: `Gas_vers_scurta` txt files excluding `*_unupload.txt`  
Output images in: `Gas_vers_scurtaout`

---


```
cd src
python MeteoGasUnupload.py
```

Input folder: `Gas_vers_scurta` txt files: `*_unupload.txt`  
Output images in: `Gas_vers_scurtaout`

---


```
cd src
python MeteoAirquixmini09.py
```

Input folder: `airquixmini09_cBivolaru/airquixmini09/GAS` txt files all including: `*_unupload.txt`  
Output images in: `airquixmini09_cBivolaru/airquixmini09/GASout`

