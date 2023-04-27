document.addEventListener("DOMContentLoaded", () => {
  const rectangles = document.querySelectorAll(".rectangle");
  const infoDialog = document.getElementById("info-dialog");

  rectangles.forEach((rectangle) => {
    rectangle.addEventListener("click", (event) => {
      const info = event.target.dataset.info;
      const status = event.target.dataset.status;
      const statusCode = event.target.dataset.statuscode;
      const moid = event.target.dataset.moid;
      infoDialog.innerHTML = info + "-" + status;

      // Create a button to make an order if the status is con_trong
      console.log(statusCode);
      if (statusCode == "CT") {
        infoDialog.innerHTML +=
          "<br /><a href='/haccanhvien/order' class='btn btn-primary'>Mua hàng</a>";
      } else if (statusCode == "DB") {
        infoDialog.innerHTML += `<br /><a href='/haccanhvien/thong-tin-nguoi-mat/add/${moid}' class='btn btn-warning'>Thêm thông tin người mất</a>`;
      }

      const rectPosition = event.target.getBoundingClientRect();
      infoDialog.style.left = `${rectPosition.left}px`;
      infoDialog.style.top = `${rectPosition.bottom + 10}px`;
      infoDialog.style.display = "block";
    });
  });

  document.addEventListener("click", (event) => {
    if (!event.target.classList.contains("rectangle")) {
      infoDialog.style.display = "none";
    }
  });
});
