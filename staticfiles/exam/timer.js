// 10 minutes countdown
(function(){
  let totalSeconds = 10 * 60; // 10 minutes
  const timeElem = document.getElementById('time');
  const form = document.getElementById('quizForm');
  const submitBtn = document.getElementById('submitBtn');

  function formatTime(s){
    let m = Math.floor(s / 60);
    let sec = s % 60;
    return m + ":" + (sec < 10 ? "0" + sec : sec);
  }

  function tick(){
    timeElem.textContent = formatTime(totalSeconds);
    if (totalSeconds <= 0) {
      // Auto-submit when time ends
      if (form) {
        // disable inputs to avoid double-submit UI race
        if (submitBtn) submitBtn.disabled = true;
        form.submit();
      }
      return;
    }
    totalSeconds--;
    setTimeout(tick, 1000);
  }

  // start when DOM loaded
  document.addEventListener('DOMContentLoaded', function(){
    tick();
  });
})();
