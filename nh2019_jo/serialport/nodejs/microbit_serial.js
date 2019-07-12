'use strict';

var SerialPort = require("serialport");

// シリアルポート設定 115200bps
const port = new SerialPort('\\\\.\\COM9', {
    baudRate: 115200
});

const ReadLine =SerialPort.parsers.Readline;
const parser = new ReadLine();

port.pipe(parser);

port.on('open', function() {
	console.log('Open');
});

// 受信待ち
port.on('data', function(data) {
	var text = String(data);
	console.log(text);
});
