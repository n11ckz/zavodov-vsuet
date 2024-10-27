package data;

import utils.Console;

public class DataFactory {
    private final Console console;

    public DataFactory(Console console) {
        this.console = console;
    }

    public Group createGroup() {
        System.out.print("Введите название группы: ");
        String name = console.readLine().toLowerCase();

        return new Group(name);
    }

    public Student createStudent() {
        System.out.print("Введите имя студента: ");
        String name = console.readLine().toLowerCase();

        System.out.print("Введите название группы: ");
        String groupName = console.readLine().toLowerCase();

        return new Student(name, groupName);
    }
}
