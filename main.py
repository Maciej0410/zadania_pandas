import numpy as np
import pandas as pd
import xlrd
import openpyxl

# zad1

dane = pd.ExcelFile('imiona.xlsx')
plik = pd.read_excel(dane, header=0)
print(plik)

# zad2

print(plik[plik['Liczba'] < 1000])
print()
print(plik[plik.Imie == 'MACIEK'])
print()
print(sum(plik['Liczba']))
print()
print(sum(plik['Liczba'] & ((plik.Rok) > 2004) & ((plik.Rok) < 2011) ))
print()
print(sum(plik['Liczba'] & ((plik.Plec) == 'M') & ((plik.Rok) == 2000) ))
print()
kobieta = plik[(plik.Plec == 'K')]
mezczyzna = plik[(plik.Plec == 'M')]
print(plik.Imie[plik.Liczba == max(mezczyzna.Liczba)])
print(plik.Imie[plik.Liczba == max(plik.Liczba)])
grupa = plik.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
print(grupa)



# zad3

plik2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
nazwiska = plik2['Sprzedawca']
nazwiska= nazwiska.unique()
print(pd.Series(nazwiska))
print()
plik2['Utarg'] = plik2['Utarg'].astype(float)
utargi = (plik2.sort_values(by='Utarg', ascending=False).head(5))
print(utargi['Utarg'])
print()
print(plik2.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))
print()
print(plik2.groupby('Kraj').agg({'Kraj':['count']}))
print()
plik2['Data zamowienia'] = plik2['Data zamowienia'].astype('datetime64[ns]')
polacy = (plik[(plik.Kraj == 'Polska') & (plik['Data zamowienia'].dt.year == 2005)])
print(polacy.groupby('Kraj').agg({'Utarg':['sum']}))
print()
rocznik_04 = plik[(plik['Data zamowienia'].dt.year == 2004)]
print(rocznik_04['Utarg'].mean())
print()
rocznik_04 = plik2[(plik2['Data zamowienia'].dt.year == 2004)]
rocznik_05 = plik2[(plik2['Data zamowienia'].dt.year == 2005)]
rocznik_04.to_csv('zamowienia_2004.csv', index=False)
rocznik_05.to_csv('zamowienia_2005.csv', index=False)