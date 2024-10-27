import data.*;
import database.Database;
import utils.Console;

public class Application {
    private final Database database;
    private final DataFactory factory;
    private final Console console;

    public Application(Database database, DataFactory factory, Console console) {
        this.database = database;
        this.factory = factory;
        this.console = console;
    }

    public void Run() {
        database.initialize();

        while (true) {
            showMenu();
            console.write("\nSelect option: ");

            String option = console.readLine();

            switch (option) {
                case "1":
                    Group group = factory.createGroup();
                    database.addGroup(group);
                    break;
                case "2":
                    console.write("Enter group name: ");
                    String groupName = console.readLine();
                    database.removeGroup(groupName);
                    break;
                case "3":
                    Student student = factory.createStudent();
                    database.addStudent(student);
                    break;
                case "4":
                    console.write("Enter student name: ");
                    String studentName = console.readLine();
                    database.removeStudent(studentName);
                    break;
                case "0":
                    System.exit(0);
                default:
                    console.writeLine("\nInvalid operation");
            }

            console.write("Press enter to continue");
            console.readLine();
            console.clear();
        }
    }

    private void showMenu() {
        console.writeLine("1. Add group \n2. Remove group\n3. Add student to group \n4. Remove student \n0. Exit");
    }
}
