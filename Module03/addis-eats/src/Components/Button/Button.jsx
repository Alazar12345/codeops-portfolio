import "./Button.css";
function Button({ text,onClick={onClick} }) {
  return (
    <button className="btn" onClick={onClick}>
      {text}
    </button>
  );
}

export default Button;