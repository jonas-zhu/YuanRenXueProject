const express = require('express');
const app = express();
var bodyParser = require('body-parser');
app.use(bodyParser());

var async = require("async");
const jsdom = require("jsdom");
const fs = require("fs");
const CryptoJS = require("crypto-js");
const {JSDOM} = jsdom;
options = {
    url: "https://match.yuanrenxue.com/match/5",
    referrer: "https://match.yuanrenxue.com/match/5",
    contentType: "text/html",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    includeNodeLocations: true,
    runScripts:"dangerously",
    pretendToBeVisual:true,
    beforeParse(window){
        window.setInterval = function(){};
        window.setInterval.toString = function(){return "function setInterval() { [native code] }"};
        window.setTimeout = function(){};
        window.setTimeout.toString = function(){return "function setTimeout() { [native code] }"};
        window.CryptoJS = CryptoJS;
    }
};


async function readFileFun () {
    let dataObj={};
    return await new Promise(function (resolve, reject) {
        result = fs.readFile("C:\\Users\\Administrator\\Desktop\\Demo\\猿人学题目\\第五题-js混淆-乱码增强\\test.html", "utf-8", function (err, data) {
            if (err) {
                reject(err);
            }
            const dom = new JSDOM(data, options);
            cookie_ = dom.window.document.cookie;
            m_ = dom.window['_$is'];
            f_ = dom.window.$_zw[23];
            dataObj["cookie"] = cookie_;
            dataObj["m"] = m_;
            dataObj["f"] = f_;
            dom.window.close();
            resolve(dataObj);
        });
    })
}


function get_cookie_m_f() {

    result = fs.readFile("C:\\Users\\Administrator\\Desktop\\Demo\\猿人学题目\\第五题-js混淆-乱码增强\\test.html", "utf-8", function (err, data) {
        var request_list = {};
        const dom = new JSDOM(data, options);
        cookie_ = dom.window.document.cookie;
        m_ = dom.window['_$is'];
        f_ = dom.window.$_zw[23];
        // console.log(cookie_);
        // console.log(m_);
        // console.log(f_);
        request_list["cookie"] = cookie_;
        request_list["m"] = m_;
        request_list["f"] = f_;

        dom.window.close();
        console.log(request_list);
        return request_list;

    });
    console.log(result);
    return result
}

// get_cookie_m_f();
app.get('/get_cookie_m_f',
    function (req, res) {
        readFileFun().then(function (dataObj) {
            res.send(dataObj);}).catch(function (err) {
                console.log(err);
                res.send(err);
            });

    }
    );

app.listen(3011, () => {
    console.log('开启服务，端口3011')
    });

