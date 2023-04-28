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
      const button_mua_hang =
        "<a href='/haccanhvien/order' class='btn btn-primary'>Mua dịch vụ</a>";
      const button_them_thong_tin_nguoi_mat = `<a href='/haccanhvien/thong-tin-nguoi-mat/add/${moid}' class='btn btn-warning'>Thêm thông tin người mất</a>`;
      const button_thong_tin_nguoi_mat = `<a href='/haccanhvien/thong-tin-nguoi-mat/${moid}' class='btn btn-info'>Thông tin người mất</a>`;

      if (statusCode == "CT") {
        infoDialog.innerHTML +=
          "<br /><a href='/haccanhvien/order' class='btn btn-primary'>Mua dịch vụ</a>";
      } else if (statusCode == "DB") {
        infoDialog.innerHTML += `<br/> ${button_mua_hang} ${button_them_thong_tin_nguoi_mat}`;
      } else if (statusCode == "DSD") {
        infoDialog.innerHTML += `<br/> ${button_mua_hang} ${button_them_thong_tin_nguoi_mat} ${button_thong_tin_nguoi_mat}`;
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
