function $(id){return document.getElementById(id);}
var str;
var result;

function display(str0)	//显示到文本框
{
	str = document.getElementById("text");
	str.value = str.value + str0;
}


function equals()	//等于
{
	str = document.getElementById("text");
	process0 = str.value;
	process = "process"+"="+str.value.replace('+','$');
	var request = new XMLHttpRequest();
	request.open('post','http://47.98.132.72/:5000/calculate');
	request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	request.send(process);
	request.onreadystatechange = function () {
		// 这步为判断服务器是否正确响应
		if (request.readyState == 4 && request.status == 200) {
			result = request.responseText;
			str.value = result;
			if(result=="算式存在错误"){
				str.value = "";
			}
			add_to_results(process0,result);
		} else {
			console.log("error");
		}
	};
}

function add_to_results(process,result){
	results = document.getElementById("results");
	console.log("123");
	last = results.value
	results.value = last + "\n" + process+"="+result;
}

function back()		//退格
{
	str = document.getElementById("text");
	str.value = str.value.substring(0,str.value.length-1);
}
function reset()	//清除
{
	str = document.getElementById("text");
	str.value = "";
}
