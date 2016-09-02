//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by John Spence on 6/8/16.
//  Copyright © 2016 John Spence. All rights reserved.
//

import Foundation

class EntitiesHelper {
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    static func getSchools() -> [Entity]! {
        if listOfSchool.isEmpty {
        let holberton = Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School)
        listOfSchool.append(holberton)
        }
        return listOfSchool
    }
    
    static func getTechCompanies() -> [Entity]! {
        if listOfTechCompany.isEmpty {
        listOfTechCompany.append(Entity(name: "LinkedIn", town: "San Franciso", imageName: "linkedin", type: .TechCompany))
        listOfTechCompany.append(Entity(name: "Docker", town: "San Franciso", imageName: "docker", type: .TechCompany))
        listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "linkedin", type: .TechCompany))
        listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
        listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
        listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
    return listOfTechCompany
}
}