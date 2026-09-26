import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema } from "../../schemas/loginSchemas";
import useAuthStore from "../../store/authStore";
import { useNavigate } from "react-router-dom";


function Login() {

  const login = useAuthStore(
    (state) => state.login
  );

  const navigate = useNavigate();


  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(loginSchema),
  });



  function onSubmit(data) {

    login(data);

    navigate("/");

  }



  return (
    <div>

      <h2>
        Login
      </h2>


      <form onSubmit={handleSubmit(onSubmit)}>


        <input
          type="email"
          placeholder="Email"
          {...register("email")}
        />


        {errors.email && (
          <p>
            {errors.email.message}
          </p>
        )}



        <input
          type="password"
          placeholder="Password"
          {...register("password")}
        />


        {errors.password && (
          <p>
            {errors.password.message}
          </p>
        )}



        <button type="submit">
          Login
        </button>


      </form>

    </div>
  );
}


export default Login;