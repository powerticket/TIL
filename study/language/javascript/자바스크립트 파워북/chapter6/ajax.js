const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

const ajax = new XMLHttpRequest();
const url = 'https://jsonplaceholder.typicode.com/todos/1/'

ajax.onload = function () {
  if (ajax.status >= 200 && ajax.status < 300) {
    successCallback(ajax.response);
  } else {
    errorCallback(new Error(ajax.statusText));
  }
};

ajax.onerror = errorCallback;
ajax.open('GET', url);
ajax.setRequestHeader('Accept', 'application/json');
ajax.send();

function successCallback (response) {
  console.log('response: ' + response)
}
function errorCallback (error) {
  console.log('error: ' + error.message)
}
