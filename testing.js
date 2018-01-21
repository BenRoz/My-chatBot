//for (var i=0; i<5 ;i++){
//    var btn = document.createElement("button");
//    btn.innerHTML = "button"+ i;
//    btn.addEventListener("click", function(){
//        console.log(i);
//    })
//    document.body.appendChild(btn);
//}
//
//
//









//for (var i=0; i<5 ;i++){
//    var btn = document.createElement("button");
//    btn.innerHTML = "button"+ i;
//    btn.data = i;
//    btn.addEventListener("click", function(){
//        console.log(this.data);
//    })
//    document.body.appendChild(btn);
//
//}
//
for (let i=0; i<5 ;i++){
    var btn = document.createElement("button");
    btn.innerHTML = "button"+ i;
    btn.addEventListener("click", function(){
        console.log(i);
    })
    document.body.appendChild(btn);

}