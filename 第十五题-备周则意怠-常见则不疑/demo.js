// https://bbs.huaweicloud.com/blogs/238330
window = global;
const fs = require('fs');
const path = require('path');
const wasmFile = fs.readFileSync(path.join(__dirname, '.', '.', './main.wasm'));
const wasm = new WebAssembly.Module(wasmFile, {});
wasm_exports= new WebAssembly.Instance(wasm, {  env: { memoryBase: 0, tableBase: 0, memory: new WebAssembly.Memory({ initial: 256, maximum: 512, }), table: new WebAssembly.Table({ initial: 0, maximum: 0, element: 'anyfunc', }), abort: console.log,  },}).exports;
t1 = parseInt(Date.parse(new Date())/1000/2);
t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
window.q = wasm_exports.encode;

function get_m(){
  window.m = function (){
              t1 = parseInt(Date.parse(new Date())/1000/2);
              t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
              return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
          };
  return window.m()
}
