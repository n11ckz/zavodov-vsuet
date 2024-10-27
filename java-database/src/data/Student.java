package data;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Student {
    public final String name;
    public final Group group;

    public final List<Boolean> Tasks = new ArrayList<>(Arrays.asList(false, false, false));

    public Student(String name, String groupName) {
        this.name = name;
        this.group = new Group(groupName);
    }
}
