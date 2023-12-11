document.getElementById("f1").addEventListener("submit", formHandler, false);
let a = 0;

setInterval(function () {
    console.log(a++)
}, 1000);

if (a === 60) console.log("111111111111111111111111111111111111111111111111");

function formHandler(event) {
    event.preventDefault();
    console.log(event);

    let elems = event.srcElement.getElementsByClassName("formBlock");
    // console.log(elems);

    for (let i = 0; i < elems.length; i++) {
        const dataBlock = document.createElement('div');

        dataBlock.appendChild(labelTag(elems[i]));

        dataBlock.appendChild(dataTag(elems[i]));

        document.getElementById('data').appendChild(dataBlock);
    }

}


function labelTag(elm) {
    // console.log(elm.getElementsByTagName("label")[0].innerHTML);
    let label = document.createElement('label');
    label.innerHTML = elm.getElementsByTagName("label")[0].innerHTML;
    return label;
}

function dataTag(elm) {
    // console.log(elm.getElementsByTagName("input")[0].value);
    let inputTagValue = document.createElement('div');
    inputTagValue.innerHTML = elm.getElementsByTagName("input")[0].value;
    return inputTagValue;
}
