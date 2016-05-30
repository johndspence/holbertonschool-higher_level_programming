//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//
//  Created by John Spence on 5/29/16.
//  Copyright © 2016 John Spence. All rights reserved.
//

import Foundation

class TechCompaniesHelper {
    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
    
    static func getTechCompanies() -> [String] {
        return self.companies
    }
}
