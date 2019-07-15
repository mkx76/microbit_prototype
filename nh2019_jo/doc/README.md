# micro:bitを使った距離計測システム

micro:bitが無線通信を実施した際に取得できる電界強度の情報をもとに  
お互いの距離を計測することができる。

## 簡易シーケンス

```mermaid
sequenceDiagram
  loop every minut
    microbitA->>microbitB: データをBluetoothで送信
    microbitB->>microbitB: 電波強度を計測
    microbitB->>microbitB: 電波強度を距離情報に変換
    microbitB->>microbitC: 距離情報をBluetoothで送信
    microbitC->>PC/RPi: 距離情報をシリアル通信で送信
    PC/RPi->>kintone: 計測データアップロード
  end
```

```mermaid
sequenceDiagram
  loop every minut
    microbitA->>microbitD: データをBluetoothで送信
    microbitD->>microbitD: 電波強度を計測
    microbitD->>microbitD: 電波強度を距離情報に変換
    microbitD->>PC/RPi: 距離情報をシリアル通信で送信
    PC/RPi->>kintone: 計測データアップロード
  end
```

## 簡易構成図

```mermaid
graph LR
  MA("micro:bit A<br />(子供用)")
  MB("micro:bit B<br />(親用)")
  MC("micro:bit C<br />(PC連携用)")
  MD("micro:bit D<br />(B&Cの統合版)")
  PC("PC/RPi3")
  KT("Kintone")

  MA-.-|BLE|MB
  MB-.-|BLE|MC
  MC-.-|BLE|MA
  MC---|Serial|PC
  MA-.-|BLE|MD
  MD---|Serial|PC
  PC-->|upload|KT
```

## Spec

### micro:bit 無線強度

signal strength: the value ranges from -128 to -42 (-128 means a weak signal and -42 means a strong one.)

## Installations

### pythonパッケージ

```python
pip3 install PySerial
```

### node.jsパッケージ

```javascript
npm install serialport
```

## Usage

### python環境

```shell
python3 microbit_serial.py
```

### node.js環境

```shell
node microbit_serial.js
```

## 拡張/発展案

micro:bitの機能に自身のシリアル番号を取得することができる。  
これを利用して個体識別をすることで、同一プログラムで複数台のmicro:bitを利用することができる。

上記で記載したシステム構成図、シーケンス図では子機側から親機に向かって情報を送信し  
親機で距離を算出しているが、親機が情報を送信しそれを受信した子機が一定の距離以内だった場合に  
応答を返す（この際にシリアル番号をつける)ことも可能。  
この場合、親機側で送信周期などを変更することが可能になるため  
改修の際などの手間を減らす事ができる。

```mermaid
graph LR
  mA[micro:bit A]
  mB[micro:bit B]
  mC[micro:bit C]
  mD[micro:bit D]
  mE[micro:bit E]
  mF[micro:bit F]
  AP1[ブランコ]
  AP2[砂場]
  AP3[すべり台]


  mA-.-|10|AP1
  AP2-.-|30|mA
  mB-.-|10|AP1
  AP3-.-|40|mB
  mC-.-|10|AP1
  mD-.-|30|AP2
  mE-.-|10|AP3
  mF-.-|10|AP2
```