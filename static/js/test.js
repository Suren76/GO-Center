<div class="yt-spec-touch-feedback-shape__fill" style=""></div>
<yt-formatted-string class="style-scope ytd-menu-service-item-renderer">Unsubscribe</yt-formatted-string>


var count = document.querySelectorAll("ytd-channel-renderer:not(.ytd-item-section-renderer)");

function myFunc() {
  for (var i = 0; i < count.length; i++){
    if (count == 0) return;
    removeSubscribtion(count[i]);
  }
}

function myFunc(i) {
    if (count == 0) return;
    removeSubscribtion(count[i]);
    return i+1;
}

function removeSubscribtion(elem) {
    el = elem.getElementsByClassName("yt-spec-touch-feedback-shape__fill")[1];
    console.log("subscribe button click");
    el.click();
    delay(10).then(() => Unsubscribe());
  }


function Unsubscribe() {
  console.log("Unsubscribe button click");
  document.getElementsByTagName("ytd-menu-service-item-renderer")[3].click();
  console.log("confirm dialog unsubscribe button click");
  delay(10).then(() => document.getElementsByTagName("yt-confirm-dialog-renderer")[0].getElementsByTagName("button")[1].click());
}

function delay(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}


  // setTimeout(function () {
  //
  //   var unSubBtn = document.getElementById("confirm-button").click();
  //   i++;
  //   count--;
  //   console.log("channel " + i + " unsubscribed");
  //
  //   setTimeout(function () {
  //     el = document.querySelector("ytd-channel-renderer");
  //     el.parentNode.removeChild(el);
  //     myTimer();
  //   }, 250);
  //
  // }, 250);




count[0].getElementsByClassName("yt-spec-touch-feedback-shape__fill")[1].click() // subscribe button click
document.getElementsByTagName("ytd-menu-service-item-renderer")[3] // Unsubscribe button click
document.getElementsByTagName("yt-confirm-dialog-renderer")[0].getElementsByTagName("button")[1].click()// confirm dialog unsubscribe button click
