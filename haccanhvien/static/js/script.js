document.addEventListener("DOMContentLoaded", () => {
  const rectangles = document.querySelectorAll(".rectangle");
  const infoDialog = document.getElementById("info-dialog");

  rectangles.forEach((rectangle) => {
    rectangle.addEventListener("click", (event) => {
      const info = event.target.dataset.info;
      infoDialog.innerHTML = info;

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
