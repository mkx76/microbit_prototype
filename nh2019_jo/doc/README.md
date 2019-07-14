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
