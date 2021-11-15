from app.controllers.gender_controller import create_gender


def main():
    create_gender('Female')
    create_gender('Male')
    create_gender('Other')


if __name__ == '__main__':
    main()