class University {
  constructor(name) {
    this.name = name;
    this.departments = [];
  }

  addDepartment(dept) {
    this.departments.push(dept);
  }

  removeDepartment(dept) {
    let index = this.departments.indexOf(dept);
    if (index !== -1) {
      this.departments.splice(index, 1);
    }
  }

  displayDepartments() {
    console.log(this.name);
    console.log(this.departments);
  }
}

let uni = new University("My University");
uni.addDepartment("Computer");
uni.addDepartment("IT");
uni.addDepartment("Mechanical");
uni.removeDepartment("Mechanical");
uni.displayDepartments();