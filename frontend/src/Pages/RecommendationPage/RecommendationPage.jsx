import React, { useEffect, useState } from 'react';
import { usePreferences } from "../../context/preferences";

export const RecommendationPage = () => {
    // const [loading, setLoading] = useState(true);
    const [citiesArray, setCitiesArray] = useState(null);
    const { preferences, setPreferences } = usePreferences();

    console.log("RECOMMENDATIONS PREFERENCES:", preferences)

    useEffect(() => {
        const interval = setInterval(() => {
            const cachedCities = preferences['recommendations']; // Get cached cities array
            // console.log(cachedCities)
            if (cachedCities) {
                setCitiesArray(cachedCities);
                // setLoading(false);
                clearInterval(interval); // Stop the interval when cities are fetched
            }
        }, 1000); // Check every 1 second for cached cities

        return () => clearInterval(interval); // Cleanup on unmount
    }, []);

    return (
        <div className="Continent">
            <h3>YOUR RECOMMENDATIONS</h3>
            {!citiesArray || citiesArray.length === 0 ? ( // Check if citiesArray is null or an empty array
                <NoRecommendationsModal />
            ) : (
                <div>
                    {citiesArray.map((continentData, index) => (
                        <div key={index}>
                            {Object.keys(continentData).map(city => (
                                <p key={city}>{city}</p>
                            ))}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};