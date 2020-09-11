alert("網站被攻擊了!");

var lis = document.getElementsByTagName("li")

for (var i = 0; i < lis.length; i++) {
    var li = lis[i]
    li.innerHTML = "持續攻擊!";
}