var str = "Hello, playground"


class Person{
    var first_name: String
    var last_name: String
    var age: Int

    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }

    func fullName() -> String{
        return self.first_name  + " " + self.last_name
    }
}

//class mentor
class Mentor: Person, Classify{
    let subject: Subject

    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }

    func isStudent() -> Bool {
        return false
    }

    func stringSubject() -> String{
        switch self.subject{
        case .Math:
            return "Math"
        case .English:
            return "English"
        case .French:
            return "French"
        case .History:
            return "History"
        }
    }
}

//class student
class Student: Person, Classify{
    func isStudent() -> Bool {
        return true
    }
}

//class school
class School {
    var name: String
    init(name: String){
        self.name = name
    }

    var list_persons = [Person!]()

    func addStudent(p: Person) -> Bool{
        if p is Student{
            list_persons.append(p)
            return true
            } else {
        return false
        }
    }

    func addMentor(p: Person) -> Bool{
        if p is Mentor{
            list_persons.append(p)
            return true
        } else {
        return false
        }
    }

}

//enumeration
enum Subject {
    case Math, English, French, History
}

//protocol
protocol Classify {
    func isStudent() -> Bool
}
