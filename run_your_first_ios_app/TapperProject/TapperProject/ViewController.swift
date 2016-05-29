//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var textfield_number: UITextField!
    
    var taps_done: Int = 0
    var taps_requested: Int? = 0
    
    //User presses Play Button after entering a number
    @IBAction func clickPlayButton(sender: AnyObject) {
        taps_requested = Int(self.textfield_number.text!)
        if self.textfield_number != nil && self.textfield_number.text != "" && taps_requested > 0 {

            if self.taps_requested != nil {
                self.image_tapper.hidden = true
                self.textfield_number.hidden = true
                self.button_play.hidden = true
                
                self.button_coin.hidden = false
                self.label_taps.hidden = false
            }
        }
    }
    
    //Click coin button appears after user clicks play
    @IBAction func clickCoinButton(sender: AnyObject) {
        taps_done += 1
        
        self.updateTapsLabel()
        
        if taps_done > taps_requested {
            self.resetGame()
        }
    }
    
    //Tells user how many taps have been achieved
    func updateTapsLabel() {
        self.label_taps.text = String(taps_done) + " Taps !"
    }
    
    //Initial and reset values
    func resetGame() {
        taps_done = 0
        taps_requested = 0
        self.textfield_number.text = ""
        self.updateTapsLabel()
        self.image_tapper.hidden = false
        self.textfield_number.hidden = false
        self.button_play.hidden = false
        self.button_coin.hidden = true
        self.label_taps.hidden = true
        
    }
    
    //Initial load
    override func viewDidLoad() {
        super.viewDidLoad()
        taps_done = 0
        taps_requested = 0
        self.image_tapper.hidden = false
        self.textfield_number.hidden = false
        self.button_play.hidden = false
        self.button_coin.hidden = true
        self.label_taps.hidden = true
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

