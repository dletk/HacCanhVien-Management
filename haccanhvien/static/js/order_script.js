document.addEventListener("DOMContentLoaded", function () {
  const customerTypeSelect = document.getElementById("customer_type");
  const newCustomer = document.getElementById("new_customer");
  const existingCustomer = document.getElementById("existing_customer");
  const mainForm = document.getElementById("main_form");
  const existingCustomerSelect = document.getElementById(
    "existing_customer_select"
  );
  const newCustomerInputs = newCustomer.querySelectorAll(
    "input, select, textarea"
  );

  function toggleNewCustomerFields(enable) {
    newCustomerInputs.forEach((input) => {
      input.disabled = !enable;
    });
  }

  customerTypeSelect.addEventListener("change", function () {
    if (this.value === "new") {
      newCustomer.style.display = "block";
      existingCustomer.style.display = "none";
      toggleNewCustomerFields(true);
    } else if (this.value === "existing") {
      newCustomer.style.display = "none";
      existingCustomer.style.display = "block";
      toggleNewCustomerFields(false);
    }
  });

  mainForm.addEventListener("submit", function (event) {
    const selectedCustomerId = existingCustomerSelect.value;
    if (selectedCustomerId) {
      const formActionUrl = `/haccanhvien/order/${selectedCustomerId}/`;
      mainForm.setAttribute("action", formActionUrl);
    } else {
      mainForm.setAttribute("action", "/haccanhvien/order/");
    }
  });
});
