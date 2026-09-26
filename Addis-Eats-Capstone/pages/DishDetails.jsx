import { useParams } from "react-router-dom";

function DishDetails() {

  const { id } = useParams();

  return (
    <div>
      <h2>Dish Details Page</h2>

      <p>
        Dish ID: {id}
      </p>

    </div>
  );
}

export default DishDetails;