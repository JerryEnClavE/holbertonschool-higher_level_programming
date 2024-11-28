addEventListener("DOMContentLoaded"), function () {
    //function ri change the color of the header element
    function changeColor () { 
        document.querySelector("header").style.color = "#FF0000";

    }

    //get the div element to wich we will apply the even tlistener
    const divRedHeader = document.querySelector("red_header");


    //Add the click evnt listerner to div element
    divRedHeader.addEventListener("click", changeColor);
});

