'use strict';

/** LCD显示器 */
var lcd;
/** 光线传感器 */
var lightSensor;

var interval;
var myDate
var isSleep = 0;

var t1,t2;

$.ready(function (error) {
    if (error) {
        console.log(error);
        return;
    }

    initSleepButton();

    lcd = $('#lcd');

    $('#lcd').turnOn();
    $('#lcd').setCursor(0, 0);
    $('#lcd').print('Welcome!');
    //每1秒更新一次时间.
    interval = setInterval(showTime, 1000);
});

function showLightIntensity() {
    lcd.clear();
    //从光照传感器获取光照强度
    lightSensor.getIlluminance(function (error, value) {
        if (error) {
            console.error(error);
            return;
        }
        console.log("Time: ");
        lcd.print('illuminance: ' + value);
    });
}

function showTime(){
	lcd.clear();
    myDate=new Date();
    var hour = myDate.getHours()+11;
    if (hour >= 24) {
    	hour = hour-24;
    }
    var minute = myDate.getMinutes()-4;
    if (minute >= 60) {
    	minute = minute-60;
    }
    var month = myDate.getMonth()+1;
    if (month > 12 ){
    	month = month -12;
    }
    lcd.setCursor(0,0);
	lcd.print("Date: "+myDate.getFullYear().toString()+"-"+month.toString()+"-"+myDate.getDate().toString());
	lcd.setCursor(0,1);
    lcd.print("Time: "+hour.toString()+":"+minute.toString()+":"+myDate.getSeconds().toString());
}

function setTime(){
    var myDate=new Date();
    myDate.setHours(17,14,0,0);
}


function initSleepButton(){
	var sleepbutton = $("#sleepbutton");
	sleepbutton.on("release",function(){
		console.log("button press")
		if (isSleep == 0){
			startRecordSleep();
			isSleep = 1
		}
		else{
			stopRecordSleep();
			isSleep = 0;
		}
	});
}

function openLED(){
	$("#led").turnOn();
	//$("#led").setRGB([25,25,112]);
	$("#led").setRGB(0x0000ff);

}

function closeLED(){
	$("#led").turnOff();
}

function getSleepQuilty(sleeptime){
    console.log("sleeptime"+sleeptime);
    var http = require("http");
    http.get("http://lxgshadow.us/pyweb/api/upload/sleeptime?slptime="+sleeptime, function(res) {
        console.log("api-sleepquilty " + res.statusCode);
        console.log(res.statusCode == "200");
        lcd.clear();
        if (res.statusCode == "200"){
            res.setEncoding('utf8');
            res.on('data', function (chunk) {
                console.log('BODY: ' + chunk);
                    var data = JSON.parse(chunk);
                if (data["code"] == "1"){
                    var quilty = data["data"]["quilty"];
                    lcd.setCursor(0, 0);
                    lcd.print('Your sleep quilty: ');
                    lcd.setCursor(0, 1);
                    lcd.print(quilty);
                }
                else{
                    lcd.setCursor(0, 0);
                    lcd.print('Get sleep quilty error');
                }
            });
        }
        else{
            lcd.setCursor(0, 0);
            lcd.print('Get sleep quilty error');
        }
    }).on('error', function(e) {
        console.log("Got error: " + e.message);
    });
    setTimeout(function(){
        interval = setInterval(showTime, 1000);
    },1000);
}



function startRecordSleep(){
    t1 = new Date();
	clearInterval(interval);
	lcd.clear();
	lcd.setCursor(0,0);
	lcd.print("Initiating...");
	lcd.setCursor(0,1);
	setTimeout(function(){
		openLED();
		lcd.print("Start Recording Sleeping");
		interval = setInterval(showTime, 1000);
	},3000);
}

function stopRecordSleep(){
	clearInterval(interval);
	lcd.clear();
	lcd.setCursor(0,0);
	lcd.print("Stopping...");
	lcd.setCursor(0,1);
	setTimeout(function(){
		closeLED();
		lcd.print("Sending Data....");
        t2 = new Date();
        getSleepQuilty(parseInt( (t2.getTime()-t1.getTime())/1000 ));
	},3000)
}


$.end(function () {
    lcd = $('#lcd');
    lcd.turnOff();
});