import { useState } from "react";

function OrderForm() {

  const [form, setForm] = useState({
    name:"",
    phone:"",
    area:""
  });

  function handleChange(e){

    setForm({
      ...form,
      [e.target.name]:e.target.value
    });

  }

  const phoneValid = /^09\d{8}$/.test(form.phone);

  function handleSubmit(e){
    e.preventDefault();

    alert("Order Submitted!");
  }

  return(

<form onSubmit={handleSubmit}>

<h2>Delivery Details</h2>

<input
name="name"
placeholder="Name"
value={form.name}
onChange={handleChange}
/>

<input
name="phone"
placeholder="TeleBirr Number"
value={form.phone}
onChange={handleChange}
/>

<input
name="area"
placeholder="Delivery Area"
value={form.area}
onChange={handleChange}
/>

<button disabled={!phoneValid}>
Place Order
</button>

{!phoneValid && form.phone.length>0 &&
<p style={{color:"red"}}>
Phone must start with 09 and contain 10 digits.
</p>}

</form>

  );

}

export default OrderForm;