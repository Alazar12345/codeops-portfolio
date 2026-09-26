import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { checkoutSchema } from "../../schemas/checkoutSchema";


function Checkout() {


const {
 register,
 handleSubmit,
 formState:{errors}
}=useForm({

 resolver:zodResolver(checkoutSchema)

});



function onSubmit(data){

 console.log("Order:", data);

}



return (

<div>

<h2>
Checkout
</h2>


<form onSubmit={handleSubmit(onSubmit)}>


<input
placeholder="Full Name"
{...register("name")}
/>

<p>
{errors.name?.message}
</p>



<input
placeholder="Phone"
{...register("phone")}
/>

<p>
{errors.phone?.message}
</p>



<textarea
placeholder="Address"
{...register("address")}
/>


<p>
{errors.address?.message}
</p>



<select {...register("payment")}>

<option value="">
Select Payment
</option>

<option value="cash">
Cash
</option>

<option value="card">
Card
</option>

</select>


<p>
{errors.payment?.message}
</p>



<button>
Place Order
</button>


</form>


</div>

);

}


export default Checkout;