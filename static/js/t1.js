
var i = 0;
var count = document.querySelectorAll(
  "ytd-channel-renderer:not(.ytd-item-section-renderer)"
);
myTimer();
function myTimer() {
  if (count == 0) return;
  el = document.querySelector(".ytd-subscribe-button-renderer");
  el.click();
  setTimeout(func1(), 250);
}

function func1 () {
  var unSubBtn = document.getElementById("confirm-button").click();
  i++;
  count--;
  console.log("channel " + i + " unsubscribed");
  setTimeout(func2(), 250);
}

function () {
  el = document.querySelector("ytd-channel-renderer");
  el.parentNode.removeChild(el);
  myTimer();
}


function combof(elem){
  el = elem.getElementsByClassName("yt-spec-touch-feedback-shape__fill")[1];
  console.log("subscribe button click");
  el.click();
  delay(10).then(() => console.log("Unsubscribe button click"));

  document.getElementsByTagName("ytd-menu-service-item-renderer")[3].click();
  console.log("confirm dialog unsubscribe button click");
  delay(10).then(() => document.getElementsByTagName("yt-confirm-dialog-renderer")[0].getElementsByTagName("button")[1].click());

}
