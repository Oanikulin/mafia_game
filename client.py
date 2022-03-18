import asyncio
import copy
import json
import random
import os
import time

import sys 
sys.path.append('..')

import grpc
import messenger_pb2
import messenger_pb2_grpc

if __name__ == '__main__':
    grpcServerAddr = os.environ.get('MESSENGER_SERVER_ADDR', 'localhost:51075')

    channel = grpc.insecure_channel(grpcServerAddr)

    stub = messenger_pb2_grpc.MaphiaStub(channel)

    while (True):
        try:
            print('Enter your name:')
            name = input()
            print('Registering at RPC server')
            stub.Connect(messenger_pb2.InitClient(author=name))
            break
        except grpc.RpcError as e:
            e.details()
            print('Please, retry with another name')

    print('Connected successfully, waiting for a game to begin')

    client_list = stub.GetClients(messenger_pb2.Empty())
    for current in client_list:
        print('User name: ', current.author)

    users = []
    while (True):
        try:
            time.sleep(0.5)
            fl = 1
            tmp = stub.WaitForGame(messenger_pb2.InitClient(author=name))
            for user in tmp:
                if (user.author == 'error'):
                    fl = 0
                users.append(user.author)
            if fl == 0:
                users = []
                continue
            role = stub.GetRole(messenger_pb2.InitClient(author=name)).text
            break
        except grpc.RpcError as rpc_error:
            pass


    print('Game is starting with users', *users, 'and role ', role)

    stub.PostMessage(messenger_pb2.ChatMessage(author=name, text="Hello everyone"))
    stub.EndDay(messenger_pb2.InitClient(author=name))

    print('End first day called')

    while (True):

        print('city goes to sleep, mafia awakens')

        print(users)

        print(name)

        if (role == 'mafia'):
            target = random.choice(users)
            while (target == name):
                target = random.choice(users)
            #suicidal mafia to check mafia loss
            #target = name
            while True:
                try:
                    stub.KillNight(messenger_pb2.InitClient(author=target))
                    break
                except grpc.RpcError as rpc_error:
                    time.sleep(5)
                    pass 

        print('mafia did the job, policeman awakens')

        if (role == 'policeman'):
            target = random.choice(users)
            while (target == name):
                target = random.choice(users)
            
            while True:
                try:
                    checker =  stub.Check(messenger_pb2.InitClient(author=target))
                    print('policeman successfully performed check')
                    if (checker.is_mafia) and (name in users):
                        stub.PostMessage(messenger_pb2.ChatMessage(author=name, text="Mafia is " + target))
                    break
                except grpc.RpcError as rpc_error:
                    time.sleep(5)
                    pass

        print('policeman goes to sleep, everyone awakens')

        while True:
            try:
                alive_users = stub.StartDay(messenger_pb2.InitClient(author=name))
                tmp = []
                for user in alive_users:
                    tmp.append(user.author)
                users = tmp
                if name not in tmp:
                    print("You are dead and cannot perform actions anymore")
                for user in users:
                    print("Alive user: ", user)
                break
            except grpc.RpcError as e:
                time.sleep(5)
                if (e.code() == grpc.StatusCode.FAILED_PRECONDITION):
                    pass
                if (e.code() == grpc.StatusCode.INVALID_ARGUMENT):
                    print("game ended, city wins");
                    print("Thank you for the game, to play another game reconnect with a different name (great UI)")
                    sys.exit(0)
                if (e.code() == grpc.StatusCode.ALREADY_EXISTS):
                    print("game ended, mafia win");
                    print("Thank you for the game, to play another game reconnect with a different name (great UI)")
                    sys.exit(0)

        morning_messages = stub.GetMessages(messenger_pb2.InitClient(author=name))
        for message in morning_messages:
            print("A message by ", message.author, " with text: ", message.text)

        target = random.choice(users)
        while (target == name):
            target = random.choice(users)

        if name in users:
            print('Voting for ', target)
            try:
                stub.VoteKill(messenger_pb2.InitClient(author=target))
            except grpc.RpcError as e:
                time.sleep(5)
                if (e.code() == grpc.StatusCode.FAILED_PRECONDITION):
                    pass
                if (e.code() == grpc.StatusCode.INVALID_ARGUMENT):
                    print("game ended, city wins");
                    print("Thank you for the game, to play another game reconnect with a different name (great UI)")
                    sys.exit(0)
                if (e.code() == grpc.StatusCode.ALREADY_EXISTS):
                    print("game ended, mafia win");
                    print("Thank you for the game, to play another game reconnect with a different name (great UI)")
                    sys.exit(0)

        print('Voting to end the day')

        stub.EndDay(messenger_pb2.InitClient(author=name))

        print('Ended a day')

        time.sleep(10)


print("Thank you for the game, to play another game reconnect with a different name (great UI)")

