console.log("Found It")

// $(document).ready(function(){
//
// });

var roomList = []

class Room {
    room_no = 0
    floor = 0
    color = ""
    constructor(room_no,floor,color) {
        this.room_no = room_no
        this.floor = floor
        this.color = color;
    }
    getRoomNo(){
        return this.room_no
    }
    getFloor(){
        return this.floor
    }
}


var singleB = 0
var doubleB = 0
var tripleB = 0
var acB = 0
var nacB = 0




function single(){
    console.log("Single Clicked")
    console.log(singleB)
    if(singleB == 0) {
        document.getElementById("single").style.background = "linear-gradient(90deg,#755bea,#ff72c0)";
        singleB = 1;
    }else {
        document.getElementById("single").style.background = "linear-gradient(90deg,#0162c8,#55e7fc)";
        singleB = 0;
    }
    mydata = {
        s: singleB,
        d: doubleB,
        t: tripleB,
        a: acB,
        n: nacB,
    }

    $.ajax(
        {
            url: "getSingle/",
            type: 'GET',
            data: mydata,
            success: function (data) {
                roomList = []
                for( i = 0; i<data.length; i++) {
                    roomList.push(new Room(data[i].room_no,data[i].floor,data[i].color));
                    console.log("Push hoise");
                    console.log(roomList.length);
                }
                updateView();
            }
        }

    )
}
function double(){
    console.log("double Clicked")
    console.log(doubleB)
    if(doubleB == 0) {
        document.getElementById("double").style.background = "linear-gradient(90deg,#755bea,#ff72c0)";
        doubleB = 1;
    }else {
        document.getElementById("double").style.background = "linear-gradient(90deg,#0162c8,#55e7fc)";
        doubleB = 0;
    }
    mydata = {
        s: singleB,
        d: doubleB,
        t: tripleB,
        a: acB,
        n: nacB,
    }

    $.ajax(
        {
            url: "getSingle/",
            type: 'GET',
            data: mydata,
            success: function (data) {
                roomList = []
                for( i = 0; i<data.length; i++) {
                    roomList.push(new Room(data[i].room_no,data[i].floor,data[i].color));
                    console.log("Push hoise");
                    console.log(roomList.length);
                }
                updateView();
            }
        }
    )
}
function triple(){
    console.log(singleB)
    if(tripleB == 0) {
        document.getElementById("triple").style.background = "linear-gradient(90deg,#755bea,#ff72c0)";
        tripleB = 1;
    }else {
        document.getElementById("triple").style.background = "linear-gradient(90deg,#0162c8,#55e7fc)";
        tripleB = 0;
    }
    mydata = {
        s: singleB,
        d: doubleB,
        t: tripleB,
        a: acB,
        n: nacB,
    }

    $.ajax(
        {
            url: "getSingle/",
            type: 'GET',
            data: mydata,
            success: function (data) {
                roomList = []
                for( i = 0; i<data.length; i++) {
                    roomList.push(new Room(data[i].room_no,data[i].floor,data[i].color));
                    console.log("Push hoise");
                    console.log(roomList.length);
                }
                updateView();
            }
        }
    )
}
function ac(){
    console.log("ac Clicked")
    console.log(singleB)
    if(acB == 0) {
        document.getElementById("ac").style.background = "linear-gradient(90deg,#755bea,#ff72c0)";
        acB = 1;
    }else {
        document.getElementById("ac").style.background = "linear-gradient(90deg,#0162c8,#55e7fc)";
        acB = 0;
    }
    mydata = {
        s: singleB,
        d: doubleB,
        t: tripleB,
        a: acB,
        n: nacB,
    }

    $.ajax(
        {
            url: "getSingle/",
            type: 'GET',
            data: mydata,
            success: function (data) {
                roomList = []
                for( i = 0; i<data.length; i++) {
                    roomList.push(new Room(data[i].room_no,data[i].floor,data[i].color));
                    console.log("Push hoise");
                    console.log(roomList.length);
                }
                updateView();
            }
        }
    )
}
function nac(){
    console.log("nac Clicked")
    console.log(nacB)
    if(nacB == 0) {
        document.getElementById("nac").style.background = "linear-gradient(90deg,#755bea,#ff72c0)";
        nacB = 1;
    }else {
        document.getElementById("nac").style.background = "linear-gradient(90deg,#0162c8,#55e7fc)";
        nacB = 0;
    }
    mydata = {
        s: singleB,
        d: doubleB,
        t: tripleB,
        a: acB,
        n: nacB,
    }

    $.ajax(
        {
            url: "getSingle/",
            type: 'GET',
            data: mydata,
            success: function (data) {
                roomList = []
                for( i = 0; i<data.length; i++) {
                    roomList.push(new Room(data[i].room_no,data[i].floor,data[i].color));
                    console.log("Push hoise");
                    console.log(roomList.length);
                }
                updateView();
            }
        }
    )
}

function clearRoom() {
    for( i=1; i<=5 ; i++){
        var parent = document.getElementById(i)
        var childs = parent.getElementsByClassName("room")
        var len = childs.length
        while( len != 0) {
            parent.removeChild(childs[0])
            len--;
        }
    }
}


function updateView() {
    clearRoom();
    console.log(roomList)
    for( i=1; i<=5 ; i++) {
        console.log("Vitore " + i)
        console.log(roomList.length)
        var parent = document.getElementById(i);
        for( r=0; r<roomList.length;r++) {
            temp = roomList[r];
            console.log(temp.floor);
            if(temp.floor == i) {
                str1 = "#exampleModal_" + temp.room_no
                str2 = "#customer-visit_" + temp.room_no
                var child = document.createElement("div");
                child.setAttribute("class",("room "+temp.color));
                var childA = document.createElement("a");
                var id = "s_"+temp.room_no;
                childA.setAttribute("id",id);
                childA.setAttribute("class","a-room");
                childA.setAttribute("data-bs-toggle","modal");
                if(temp.color == "green") {
                    childA.setAttribute("data-bs-target",str1);
                }else {
                    childA.setAttribute("data-bs-target",str2);
                }
                childA.setAttribute("data-bs-whatever","@mdo");
                childA.setAttribute("href","#");
                childA.innerHTML = temp.room_no;
                child.appendChild(childA);
                parent.appendChild(child);
                console.log(child);
                console.log(childA);
                console.log(parent);
            }
        }
    }
}




