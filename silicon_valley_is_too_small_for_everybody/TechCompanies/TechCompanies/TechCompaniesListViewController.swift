//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by John Spence on 6/8/16.
//  Copyright © 2016 John Spence. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {

    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    let techDetailSegue = "techDetailSegue"
    
    var sectionNames:[String] = ["Schools", "Tech Companies"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Entity List"
        
        schoolList = EntitiesHelper.getSchools()
        techCompanyList = EntitiesHelper.getTechCompanies()
        
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return sectionNames.count
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return (section == 0 ? schoolList.count : techCompanyList.count)
        }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)

        // Configure the cell...
        
        if indexPath.section == 0 {
            // -- School List
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = "I Love Studying"
        }
        else {
            // -- Tech Company List
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = "I Love Working"
        }

        return cell
    }
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if section == 0
        {
            return "Schools"
        }
        if section == 1
        {
            return "Tech Companies"
        }
        return nil
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "techDetailSegue" {
            let destVC = segue.destinationViewController as? TechCompaniesDetailViewController
            let sectionSelected = tableView.indexPathForSelectedRow?.section
            let rowSelected = tableView.indexPathForSelectedRow?.row
            let list = sectionSelected == 0 ? schoolList : techCompanyList
            destVC?.entity = list[rowSelected!]
        }
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    

}
