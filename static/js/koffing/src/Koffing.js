"use strict";

import Pokemon from "./Pokemon.js";
import PokemonTeam from "./PokemonTeam.js";
import PokemonTeamSet from "./PokemonTeamSet.js";
import ShowdownParser from "./ShowdownParser.js";

class Koffing {
    /**
     * Converts from Showdown to a PokemonTeamSet object.
     *
     * @param {String|Pokemon|PokemonTeam|PokemonTeamSet|ShowdownParser} data Showdown code or object
     * @returns {PokemonTeamSet}
     */
    static parse(data) {
        if (
            data instanceof PokemonTeamSet
            || data instanceof PokemonTeam
            || data instanceof Pokemon
        ) {
            return data;
        }
        if (data instanceof ShowdownParser) {
            return data.parse();
        }
        return (new ShowdownParser(data)).parse();
    }

    /**
     * Prettifies and sanitizes the given Showdown code.
     *
     * @param {String|Pokemon|PokemonTeam|PokemonTeamSet|ShowdownParser} data Showdown code or object
     * @returns {String}
     */
    static format(data) {
        return this.parse(data).toShowdown();
    }

    /**
     * Converts from Showdown to JSON code.
     *
     * @param {String|Pokemon|PokemonTeam|PokemonTeamSet|ShowdownParser} data Showdown code or object
     * @returns {String}
     */
    static toJson(data) {
        return this.parse(data).toJson();
    }

    /**
     * Converts from JSON to Showdown code.
     *
     * @param {String|Object|Pokemon|PokemonTeam|PokemonTeamSet|ShowdownParser} data JSON code or object
     * @returns {String}
     */
    static toShowdown(data) {
        if (
            data instanceof PokemonTeamSet
            || data instanceof PokemonTeam
            || data instanceof Pokemon
        ) {
            return data.toShowdown();
        }
        if (data instanceof ShowdownParser) {
            return data.parse().format();
        }
        if (typeof value === 'string' || value instanceof String) {
            data = JSON.parse(data);
        }
        return PokemonTeamSet.fromObject(JSON.parse(data)).toShowdown();
    }
}

export {
    Koffing,
    ShowdownParser
};