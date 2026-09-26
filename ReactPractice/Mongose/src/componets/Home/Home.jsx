import { useState } from "react";
import Hero from "../Hero/Hero"
import CategoryBar from "../CategoryBar/CategoryBar";
import FeaturedSection from "../FeaturedSection/FeaturedSection"
import SearchBar from "../searchBar/searchBar";

function Home({addToCart}){
     const [selectedCategory, setSelectedCategory] = useState("All");
     const [searchTerm, setSearchTerm] = useState("");
    return(
        <div>
            <SearchBar 
            searchTerm={searchTerm}
            setSearchTerm={setSearchTerm}
            />
            <Hero/>
             <CategoryBar
        selectedCategory={selectedCategory}
        setSelectedCategory={setSelectedCategory}
      />
            <FeaturedSection addToCart={addToCart}
            selectedCategory={selectedCategory}
            searchTerm={searchTerm}
            />
        </div>
    )
}
export default Home