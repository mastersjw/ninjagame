
// var ninja = document.getElementById('ninja-pic');
// var left = parseInt(ninja.style.left);
// var bottom = parseInt(ninja.style.bottom);
// var width = parseInt(ninja.style.width);


step = 1;
animation_ran = false;
// var moveForm = document.getElementById('move');



function animate_move_left(step=1) {
    var moveForm = document.getElementById('move');
    var ninja = document.getElementById('ninja-pic');
    var left = parseInt(ninja.style.left);
    var bottom = parseInt(ninja.style.bottom);
    var width = parseInt(ninja.style.width);
    console.log("here");
    left += 30;
    ninja.style.left = left + "px";
    if (step==1) {
        step = 2;
        ninja.src= "/static/img/right2.png";
    }
    else{
        step =1;
        ninja.src="/static/img/right1.png"
    }
    
    if (left < 450) {
        setTimeout(function () {
            animate_move_left(step)}, 300)
    }
    else{
        let hiddenField = document.getElementById('direct');
        hiddenField.value = "E";
        moveForm.submit();
    }
}

function animate_move_right(step=1) {
    var ninja = document.getElementById('ninja-pic');
var left = parseInt(ninja.style.left);
var bottom = parseInt(ninja.style.bottom);
var width = parseInt(ninja.style.width);
    var moveForm = document.getElementById('move');
    if (step==1) {
        step =2;
        ninja.src= "/static/img/left2.png";
    }
    else{
        step =1;
        ninja.src="/static/img/left1.png"
    }
    left -= 20;
    ninja.style.left = left + "px";
    if (left > 20 ) {
        setTimeout(function () {
            animate_move_right(step)}, 300)
    }
    else{
        let hiddenField = document.getElementById('direct');
        hiddenField.value = "W";
        moveForm.submit();
    }
}

function animate_move_up(step=1) {
    var ninja = document.getElementById('ninja-pic');
var left = parseInt(ninja.style.left);
var bottom = parseInt(ninja.style.bottom);
var width = parseInt(ninja.style.width);
    var moveForm = document.getElementById('move');
    if (step==1) {
        step =2;
        ninja.src= "/static/img/top2.png";
    }
    else{
        step =1;
        ninja.src="/static/img/top1.png"
    }
    bottom += 10;
    width -=2;
    ninja.style.bottom = bottom + "px";
    ninja.style.width = width+"px";
    if (bottom < 160 ) {
        setTimeout(function () {
            animate_move_up(step)}, 300)
    }
    else{
        let hiddenField = document.getElementById('direct');
        hiddenField.value = "N";
        moveForm.submit();
    }
}

function animate_move_down(step=1) {
    var ninja = document.getElementById('ninja-pic');
var left = parseInt(ninja.style.left);
var bottom = parseInt(ninja.style.bottom);
var width = parseInt(ninja.style.width);
    var moveForm = document.getElementById('move');
    if (step==1) {
        step =2;
        ninja.src= "/static/img/down2.png";
    }
    else{
        step =1;
        ninja.src="/static/img/down1.png"
    }
    width +=3;
    bottom -= 10;
    ninja.style.bottom = bottom + "px";
    ninja.style.width = width+"px";
    if (bottom > -80 ) {
        setTimeout(function () {
            animate_move_down(step)}, 300)
    }
    else{
        let hiddenField = document.getElementById('direct');
        hiddenField.value = "S";
        moveForm.submit();
    }
}

function slp(a = 1,dark = true){
    let game = document.getElementById("game");
    if (document.getElementById("sleep-div")==null) {
        game.innerHTML = game.innerHTML+"<div id='sleep-div' style ='position:absolute; width:100%; height:100%; background: rgba(0,0,0,.1)'></div> ";
    }
    else{ 
        div = document.getElementById("sleep-div");
        x = 'background-color';
        test = 'rgba(0,0,0,' + (a/10) + ')';
        
        div.style.background = test;
    } 
    if ((a/10) < 1.2 && dark ==true) {
        a+=1;
        if ((a/10)>1.1) dark = false;
        setTimeout(function(){slp(a,dark)},500);
        
    }
    else if((a/10)>0 && dark == false){
        a-=1;
        setTimeout(function(){slp(a,dark)},500)
        
    } 
    else document.getElementById("sleep-form").submit();
    
}

function balance(e){
    // get labels
    let strength = document.getElementById("strength");
    let dexterity = document.getElementById("dexterity");
    let intelligence=document.getElementById("intelligence");
    //get the actual progress bar
    let st = document.getElementById("st");
    let dex = document.getElementById("dex");
    let it = document.getElementById("it");
    let max = document.getElementById("max");
    let maxPoints = 17;
    let totalPoints = parseInt(strength.value)+ parseInt(dexterity.value)+parseInt(intelligence.value);
    if(totalPoints>maxPoints){
        let overPoints = totalPoints-maxPoints;
        if(e.id == "strength"){
            
            while(overPoints>0){
                if(parseInt(dexterity.value)>1){
                    dexterity.value = parseInt(dexterity.value) -1;
                    overPoints--;
                }
                if(parseInt(intelligence.value)>1 && overPoints >0){
                    intelligence.value = parseInt(intelligence.value) -1;
                    overPoints--;
                }
            }
        }
        else if(e.id=="intelligence"){
            
            while(overPoints>0){
                if(parseInt(dexterity.value)>1){
                    dexterity.value = parseInt(dexterity.value) -1;
                    overPoints--;
                }
                
                if(parseInt(strength.value)>1 && overPoints >0){
                    strength.value = parseInt(strength.value) -1;
                    overPoints--;
                }
            }
        }
        else{
            
            while(overPoints>0){
                if(parseInt(intelligence.value)>1){
                    intelligence.value = parseInt(intelligence.value) -1;
                    overPoints--;
                }
                if(parseInt(strength.value)>1 && overPoints >0){
                    strength.value = parseInt(strength.value) -1;
                    overPoints--;
                }
            }
        }
    }
    totalPoints = parseInt(strength.value)+ parseInt(dexterity.value)+parseInt(intelligence.value);
    st.innerText="Strength: "+strength.value;
    dex.innerText="Dexterity: "+dexterity.value;
    it.innerText="Intelligence: "+intelligence.value;
    max.innerText="Points to Use: "+ (maxPoints-totalPoints);
}




