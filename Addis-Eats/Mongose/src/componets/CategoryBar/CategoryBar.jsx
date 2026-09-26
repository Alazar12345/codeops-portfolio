import "./CategoryBar.css"
function CategoryBar({ selectedCategory, setSelectedCategory }){
    const categories =[
        "All",
        "Main",
        "Vegetarian",
        "Drinks",
        "Desserts",
        "Stew",
    ];
    return(
        <div className="category-bar">
            {categories.map(category => (
                <button 
                key={category}
                className={
                    selectedCategory === category ?"active"
                    :""
                }onClick={()=> setSelectedCategory(category)}
                >{category}</button>
            ))}
        </div>
    );
}
export default CategoryBar;