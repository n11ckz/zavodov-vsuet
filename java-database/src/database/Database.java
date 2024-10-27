package database;

import data.*;
import utils.Console;

import java.sql.*;

public class Database {
    private final DatabaseConnector connector = new DatabaseConnector();

    private final Console console;

    public Database(Console console) {
        this.console = console;
    }

    public void initialize() {
        try (Connection connection = connector.getConnection(); Statement statement = connection.createStatement()) {
            String createGroupsTable = "CREATE TABLE IF NOT EXISTS GROUPS" +
                    "(ID INT AUTO_INCREMENT PRIMARY KEY," +
                    "NAME VARCHAR(16) NOT NULL UNIQUE," +
                    "STUDENT_COUNT INT DEFAULT 0)";
            statement.execute(createGroupsTable);

            String createStudentsTable = "CREATE TABLE IF NOT EXISTS STUDENTS" +
                    "(ID INT AUTO_INCREMENT PRIMARY KEY," +
                    "NAME VARCHAR(16) NOT NULL," +
                    "GROUP_NAME VARCHAR(16) NOT NULL," +
                    "TASK_1 BOOLEAN DEFAULT FALSE, TASK_2 BOOLEAN DEFAULT FALSE, TASK_3 BOOLEAN DEFAULT FALSE," +
                    "FOREIGN KEY(GROUP_NAME) REFERENCES GROUPS(NAME) ON DELETE CASCADE)";
            statement.execute(createStudentsTable);
        } catch (SQLException exception) {
            console.writeLine(exception.getMessage());
        }
    }

    public void addGroup(Group group) {
        try (Connection connection = connector.getConnection(); Statement statement = connection.createStatement()) {
            String addGroupQuery = String.format("INSERT INTO GROUPS(NAME) VALUES('%s')", group.name);
            statement.execute(addGroupQuery);

            console.writeLine("Group has been added");
        } catch (SQLException exception) {
            console.writeLine(exception.getMessage());
        }
    }

    public void removeGroup(String groupName) {
        try (Connection connection = connector.getConnection(); Statement statement = connection.createStatement()) {
            String removeGroupQuery = String.format("DELETE FROM GROUPS WHERE NAME = '%s'", groupName.toLowerCase());
            statement.execute(removeGroupQuery);

            System.out.println("Group has been removed");
        } catch (SQLException exception) {
            console.writeLine(exception.getMessage());
        }
    }

    public void addStudent(Student student) {
        try (Connection connection = connector.getConnection(); Statement statement = connection.createStatement()) {
            String isGroupExistsQuery = String.format("SELECT COUNT(*) FROM GROUPS WHERE NAME = '%s'", student.group.name);
            ResultSet resultSet = statement.executeQuery(isGroupExistsQuery);

            if (isGroupNotExists(resultSet)) {
                addGroup(student.group);
            }

            String addStudentQuery = String.format("INSERT INTO STUDENTS (NAME, GROUP_NAME) VALUES ('%s', '%s')", student.name, student.group.name);
            statement.execute(addStudentQuery);

            updateStudentCountInGroup(student.group.name, statement);

            console.writeLine("Student has been added");
        } catch (SQLException exception) {
            console.writeLine(exception.getMessage());
        }
    }

    public void removeStudent(String studentName) {
        try (Connection connection = connector.getConnection(); Statement statement = connection.createStatement()) {
            String getGroupNameQuery = String.format("SELECT GROUP_NAME FROM STUDENTS WHERE NAME = '%s'", studentName);
            ResultSet resultSet = statement.executeQuery(getGroupNameQuery);

            String groupName = "";

            if (resultSet.next()) {
                groupName = resultSet.getString("GROUP_NAME");
                console.writeLine(groupName);
            }

            String removeStudentQuery = String.format("DELETE FROM STUDENTS WHERE NAME = '%s'", studentName.toLowerCase());
            statement.execute(removeStudentQuery);

            updateStudentCountInGroup(groupName, statement);

            console.writeLine("Student has been removed");
        } catch (SQLException exception) {
            console.writeLine(exception.getMessage());
        }
    }

    private void updateStudentCountInGroup(String groupName, Statement statement) throws SQLException {
        String updateCountQuery = String.format("UPDATE GROUPS SET STUDENT_COUNT = " +
                "(SELECT COUNT(*) FROM STUDENTS WHERE GROUP_NAME = '%1$s') WHERE NAME = '%1$s'", groupName);
        statement.execute(updateCountQuery);
    }

    private boolean isGroupNotExists(ResultSet resultSet) throws SQLException {
        return resultSet.next() && resultSet.getInt(1) == 0;
    }
}
