def get_actors():
    """
    Returns a dictionary of actors and their respective use cases.
    
    Each actor represents a role in the PHTRS system and has specific actions they can perform.
    """
    return {
        "Citizen": [
            "Report Pothole",
            "Report Damage",
            "View Repair Status"
        ],
        "Public Works Department (PWD) Employee": [
            "Track Repair Status",
            "Assign Repair Crew",
            "Generate Repair Cost Report"
        ],
        "Repair Crew": [
            "Execute Repairs and Update Repair Status"
        ],
        "System Administrator": [
            "Manage User Accounts",
            "Manage System Configurations"
        ]
    }


def get_use_cases():
    """
    Returns a dictionary of use cases with include and extend relationships.

    - 'includes': Specifies mandatory steps required to complete the use case.
    - 'extends': Represents optional or conditional functionality that extends the main use case.
    """
    return {
        "Report Pothole": {
            "includes": [
                "Log in to the system", 
                "Enter Pothole Details", 
                "Validate Details", 
                "Submit the Report"
            ],
            "extends": []
        },
        "View Repair Status": {
            "includes": [
                "Log in to the system", 
                "Search for pothole by ID or location", 
                "View repair status and detail report"
            ],
            "extends": []
        },
        "Assign Repair Crew": {
            "includes": [
                "Log in to the system",
                "Review Pothole details and priority",
                "Assign repair crew",
                "Notify the repair crew"
            ],
            "extends": []
        },
        "Execute Repairs and Update Repair Status": {
            "includes": [
                "Log in to the system", 
                "Access Assigned Pothole Details",
                "Update Repair Status",
                "Enter Repair Details",
                "Submit the Work Order"
            ],
            "extends": ["Temporary Repair", "Request Additional Resources"]
        },
        "Track Repair Status": {
            "includes": [
                "Log in to the system",
                "Search for pothole by ID or location", 
                "Track repair status and detail report"
            ],
            "extends": []
        },
        "Report Damage": {
            "includes": [
                "Log in to the system",
                "Enter the damage details",
                "Submit the damage claim"
            ],
            "extends": []
        },
        "Generate Repair Cost Report": {
            "includes": [
                "Log in to the system",
                "Select the time period and district",
                "Generate and view the report"
            ],
            "extends": ["Export Report"]
        },
        "Manage User Accounts": {
            "includes": [
                "Log in to the system",
                "Add user",
                "Update user",
                "Delete user"
            ],
            "extends": ["Reset Password", "Audit User Activity"]
        },
        "Manage System Configurations": {
            "includes": ["Log in to the system"],
            "extends": ["Backup System Data", "Restore System Data"]
        }
    }


def print_actors(actors):
    """
    Prints actors and their respective use cases in a structured format.

    Args:
        actors (dict): A dictionary containing actors as keys and their use cases as values.
    """
    print("Actors and Their Use Cases:")
    for actor, use_cases in actors.items():
        print(f"- {actor}:")
        for use_case in use_cases:
            print(f"  - {use_case}")
    print()


def print_use_cases(use_cases):
    """
    Prints use cases along with their include and extend relationships.

    Args:
        use_cases (dict): A dictionary containing use cases, their included steps, and extensions.
    """
    print("Use Cases with Include and Extend Relationships:")
    for use_case, relationships in use_cases.items():
        print(f"Use Case: {use_case}")
        if relationships["includes"]:
            print("  Includes:")
            for include in relationships["includes"]:
                print(f"    - {include}")
        if relationships["extends"]:
            print("  Extends:")
            for extend in relationships["extends"]:
                print(f"    - {extend}")
        print()


def print_description():
    """
    Prints a brief description of the UML Use Case Diagram for the PHTRS system.
    The updated description includes details about how the system works in practice, including the data collected for each pothole,
    work orders, and reported damage.
    """
    
    print("Brief Description of the UML Use Case Diagram:")
    print("************************************************")
    print("""
    The PHTRS (Pothole and Highway Traffic Repair System) allows citizens to report potholes and damage claims through an online platform. 
    Citizens can log onto the website and report the location and severity of potholes. As potholes are reported, they are logged 
    within the 'Public Works Department Repair System' and assigned an identifying number. The system stores details such as street address, 
    pothole size (on a scale of 1 to 10), location (middle of the road, curb, etc.), district (determined by the street address), 
    and repair priority (based on the size of the pothole).

    Work order data are associated with each pothole, which includes:
    - Pothole location and size
    - Repair crew identifying number
    - Number of people on the crew
    - Equipment assigned
    - Hours applied to repair
    - Hole status (e.g., work in progress, repaired, temporary repair, not repaired)
    - Amount of filler material used
    - Cost of repair (calculated based on hours, number of people, materials, and equipment used)

    Additionally, a damage file is created to hold information about any damage reported due to the pothole. This file includes:
    - Citizen’s name, address, and phone number
    - Type of damage (e.g., vehicle damage, property damage)
    - Dollar amount of damage reported

    The system ensures that citizens can report issues easily and track repair progress, while also assisting the Public Works Department in managing and prioritizing repair tasks efficiently.
    """)


def main():
    """
    Main function that executes the sequence of printing:
    1. Actors and their use cases.
    2. Use cases with include and extend relationships.
    3. A brief system description.
    """
    actors = get_actors()      # Retrieve actors and their use cases
    use_cases = get_use_cases()  # Retrieve use cases and relationships

    print_actors(actors)        # Print actors and their use cases
    print_use_cases(use_cases)  # Print use cases with relationships
    print_description()         # Print system description


# Ensures that the script runs only when executed directly (not when imported as a module)
if __name__ == "__main__":
    main()
