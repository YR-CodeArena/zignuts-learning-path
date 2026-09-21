class University {
  constructor(name) {
    this.name = name;
    this.departments = [];
  }

  addDepartment(department) {
    this.departments.push(department);
  }

  removeDepartment(department) {
    let newDepartments = [];
    for (let i = 0; i < this.departments.length; i++) {
      if (this.departments[i] !== department) {
        newDepartments.push(this.departments[i]);
      }
    }
    this.departments = newDepartments;
  }

  displayDepartments() {
    console.log(this.name + " Departments:");
    for (let i = 0; i < this.departments.length; i++) {
      console.log(this.departments[i]);
    }
  }
}

const myUni = new University("Gujarat Technological University");
myUni.addDepartment("Computer Engineering");
myUni.addDepartment("Information Technology");
myUni.addDepartment("Mechanical Engineering");
myUni.removeDepartment("Mechanical Engineering");
myUni.displayDepartments();